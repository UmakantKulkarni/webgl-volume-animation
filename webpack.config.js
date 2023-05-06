const HtmlWebpackPlugin = require("html-webpack-plugin");
const path = require("path");

module.exports = {
  entry: "./src/app.js",
  mode: "development",
  output: {
    filename: "main.js",
    path: path.resolve(__dirname, "dist"),
  },
  devServer: {
    port: 9000,
    host: "0.0.0.0",
  },
  module: {
    rules: [
      {
        test: /\.(png|jpg|jpeg)$/i,
        type: "asset/resource",
      },
      {
        // Embed GLSL files as strings
        test: /\.(glsl|vert|frag)$/i,
        type: "asset/source",
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: "./index.html",
    }),
  ],
};
