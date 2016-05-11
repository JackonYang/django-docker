/**
 * webpack Config
 * 配置独立项、入口文件、输出项信息
 */
var webpack = require('webpack');
var fs = require('fs');  // file system
var path = require('path');
var node_modules_dir = path.join(__dirname, 'node_modules');
var components_dir = path.join(__dirname, 'components');
var views_dir = path.join(__dirname,'views');
var output_dir = path.join(__dirname, '../backend');

var entrys = {};
fs.readdirSync(views_dir).forEach(function (name, idx) {
    entrys[name] = path.join(views_dir, name, name+'.js')
});


config = {
  entry: entrys,
  output: {
    path: output_dir,
    filename: "static/[name].js"
  },
  module: {
    loaders: [
      {
        test: /\.html$/,
        loader: 'file-loader?name=templates/[name].[ext]'
      },
    ]
  }
};


module.exports = config;
