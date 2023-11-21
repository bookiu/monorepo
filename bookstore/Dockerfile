FROM golang:1.21-bookworm AS builder

ENV GOPROXY="https://goproxy.cn,direct"

WORKDIR /usr/src/app

COPY go.mod go.sum ./
RUN go env -w GO111MODULE=on && \
    go env -w GOPROXY="https://goproxy.cn,direct" &&  \
    go mod download && go mod verify

COPY . .

RUN go build -v -o /usr/src/app/bookstore-api ./cmd/bookstore


FROM docker.io/yaxin/debian

WORKDIR /app

COPY --from=builder /usr/src/app/bookstore-api /app/bookstore-api

CMD [ "/app/bookstore-api" ]
