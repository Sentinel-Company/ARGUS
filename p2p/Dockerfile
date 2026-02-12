FROM rust:1.74
WORKDIR /usr/src/app
COPY . .
RUN cargo build --release
CMD ["./target/release/argus-p2p-node"]
