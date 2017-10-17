<<<<<<< HEAD
var path = require('path');
var webpack = require('webpack');
=======
var path = require("path");
var webpack = require("webpack");
>>>>>>> 2f4830a360b6bf551a5a6114310efd4416f5ea1b

module.exports = {
  entry: "./src/main.js",
  output: {
    path: path.resolve(__dirname, "./dist"),
    publicPath: "/dist/",
    filename: "build.js"
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: "vue-loader",
        options: {
          loaders: {}
          // other vue-loader options go here
        }
      },
      {
        test: /\.js$/,
        loader: "babel-loader",
        exclude: /node_modules/
      },
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: "file-loader",
        options: {
          name: "[name].[ext]?[hash]"
        }
      },
      {
<<<<<<< HEAD
        test: /\.(gql|graphql)$/,
        loader: 'graphql-tag/loader'
=======
        test: /\.css$/,
        use: [{ loader: "style-loader" }, { loader: "css-loader" }]
>>>>>>> 2f4830a360b6bf551a5a6114310efd4416f5ea1b
      }
    ]
  },
  resolve: {
    alias: {
<<<<<<< HEAD
      vue$: 'vue/dist/vue.esm.js'
=======
      vue$: "vue/dist/vue.esm.js"
>>>>>>> 2f4830a360b6bf551a5a6114310efd4416f5ea1b
    }
  },
  devServer: {
    historyApiFallback: true,
    noInfo: true
  },
  performance: {
    hints: false
  },
<<<<<<< HEAD
  devtool: '#eval-source-map'
};

if (process.env.NODE_ENV === 'production') {
  module.exports.devtool = '#source-map';
=======
  devtool: "#eval-source-map"
};

if (process.env.NODE_ENV === "production") {
  module.exports.devtool = "#source-map";
>>>>>>> 2f4830a360b6bf551a5a6114310efd4416f5ea1b
  // http://vue-loader.vuejs.org/en/workflow/production.html
  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.DefinePlugin({
      "process.env": {
        NODE_ENV: '"production"'
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      sourceMap: true,
      compress: {
        warnings: false
      }
    }),
    new webpack.LoaderOptionsPlugin({
      minimize: true
    })
  ]);
}
