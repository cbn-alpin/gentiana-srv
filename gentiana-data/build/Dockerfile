ARG GENTIANA_DATA_IMAGE

FROM ${GENTIANA_DATA_IMAGE}

ARG UID
ARG GID
ARG LOCAL_USER

USER root
# Add the group (if not existing) then add the user to the group
RUN id --group ${LOCAL_USER} || \
        addgroup --gid ${GID} ${LOCAL_USER} && \
    id --user ${LOCAL_USER} || \
        adduser --gecos GECOS --disabled-password --uid ${UID} --gid ${GID} ${LOCAL_USER}