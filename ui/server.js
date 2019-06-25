const express = require("express");
const proxy = require("http-proxy-middleware");
const next = require("next");

const port = parseInt(process.env.EXPRESS_PORT) || 3000;
const isDev = process.env.NODE_ENV !== "production";

const app = next({ dev: isDev });
const handle = app.getRequestHandler();

app.prepare().then(() => {
  const server = express();

  server.get("*", (req, res) => {
    return handle(req, res);
  });

  server.listen(port, err => {
    if (err) throw err;
    console.log(`> Ready on http://localhost:${port}`);
  });
});
