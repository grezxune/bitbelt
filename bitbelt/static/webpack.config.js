const webpack = require('webpack');
const path = require('path');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

const CSSExtract = new ExtractTextPlugin('styles.css');

const config = {
    entry:  {
        index: path.join(__dirname, 'js', 'index.js'),
        'project-list': path.join(__dirname, 'js', 'pages', 'project-list.js'),
        project: path.join(__dirname, 'js', 'pages', 'project.js'),
    },
    output: {
        path: path.join(__dirname, 'dist'),
        filename: '[name].bundle.js',
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: 'babel-loader'
            },
            {
                test: /\.s?css$/,
                use: ExtractTextPlugin.extract({
                    use: [
                        {
                            loader: 'css-loader',
                            options:
                                {
                                    sourceMap: true
                                }
                        },
                        {
                            loader: 'sass-loader',
                            options:
                                {
                                    sourceMap: true
                                }
                        }
                    ]
                })
            },
        ]
    },
    plugins: [
        new ExtractTextPlugin('styles.css')
    ]
};



module.exports = config;