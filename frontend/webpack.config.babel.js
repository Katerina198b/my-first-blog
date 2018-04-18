import webpack from 'webpack'
var path = require('path')

var jsonImporter = require("node-sass-json-importer");
'use strict';

module.exports = {
    entry: './app.jsx',
    output: {
        path: `${__dirname}/compiled`,
        filename: "[name].js"
    },
    module: {
        loaders: [
            {
                test: /\.(js|jsx)$/,
                loader: 'babel-loader',
                exclude: '/node-modules/',
                include: [
                  path.resolve(__dirname, '')
                ],
                query: {
                    presets: ['es2015', 'react']
                }
            },
            {
                test: /\.(sass|scss|css)$/,
                loader: 'style-loader!css-loader!sass-loader'
            },
            {test: /\.(png|jpg|gif)$/, loader: "url-loader"},
        ]
    },
    resolve: {
        extensions: ['.js', '.jsx', '.'],
    },
    plugins: [
        new webpack.LoaderOptionsPlugin({
            options: {
                sassLoader: {
                    importer: jsonImporter,
                },
                context: __dirname,
            },
        }),
    ],
    // sassLoader: {
    //   includePaths: [
    //     path.resolve(__dirname, "./frontend"),
    //   path.resolve(__dirname, "./frontend/bootstrap/scss")
    // ]
    //}
}