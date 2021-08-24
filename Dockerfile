FROM jupyter/datascience-notebook:python-3.8.8

ARG USERNAME=jovyan

RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/home/jovyan/commandhistory/.bash_history" \
    && mkdir /home/jovyan/commandhistory \
    && touch /home/jovyan/commandhistory/.bash_history \
    && echo $SNIPPET >> "/home/$USERNAME/.bashrc"

WORKDIR /app
COPY . /app

USER root

RUN apt-get update && \
    apt-get install -y ruby-full build-essential && \
    apt-get install -y --no-install-recommends libicu66 gnome-keyring libsecret-1-0 desktop-file-utils x11-utils && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN chown -R jovyan:users /app

USER $NB_UID