FROM registry.access.redhat.com/ubi9/python-312

USER root
RUN groupadd -g 65532 mcpgroup && \
    useradd -u 65532 -g mcpgroup mcpuser

WORKDIR /server

COPY uv.lock pyproject.toml Makefile LICENSE README.md .
COPY server/ server/
RUN make install-uv install-global

RUN chown -R mcpuser:mcpgroup /server

USER mcpuser
EXPOSE 9001

CMD ["openstack_mcp_server"]
