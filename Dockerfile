FROM ghcr.io/astral-sh/uv:0.8.14-python3.13-bookworm-slim
COPY --from=ghcr.io/astral-sh/uv:0.7.21 /uv /uvx /bin/
ADD . /rent_due_email
WORKDIR /rent_due_email
RUN uv sync --locked
CMD ["uv", "run", "rent_due_email.py"]