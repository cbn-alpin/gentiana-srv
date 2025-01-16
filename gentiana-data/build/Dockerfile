ARG GENTIANA_DATA_IMAGE

FROM ${GENTIANA_DATA_IMAGE}

ARG UID
ARG GID
ARG LOCAL_USER

USER root
# Add the group (if not existing) then add the user to the group
RUN id --name --group ${GID} || \
        addgroup --gid ${GID} ${LOCAL_USER} && \
    id --name --user ${UID} || \
        adduser --gecos GECOS --disabled-password --uid ${UID} --gid ${GID} ${LOCAL_USER}