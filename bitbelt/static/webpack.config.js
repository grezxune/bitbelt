const webpack = require('webpack');
const path = require('path');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

const CSSExtract = new ExtractTextPlugin('styles.css');

const config = {
    entry:  {
        index: path.join(__dirname, 'js', 'index.js'),
        'project-list': path.join(__dirname, 'js', 'pages', 'project-list.js'),
        'client-list': path.join(__dirname, 'js', 'pages', 'client-list.js'),
        client: path.join(__dirname, 'js', 'pages', 'client.js'),
        project: path.join(__dirname, 'js', 'pages', 'project.js'),
        'cabinet-opening': path.join(__dirname, 'js', 'pages', 'cabinet-opening.js'),
        'project-cutlist': path.join(__dirname, 'js', 'pages', 'project-cutlist.js'),
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
            {
                test: /.(ttf|otf|eot|svg|woff(2)?)(\?[a-z0-9]+)?$/,
                use: [{
                  loader: 'file-loader',
                  options: {
                        name: '[name].[ext]',
                        outputPath: 'fonts/',    // where the fonts will go
                        publicPath: './'       // override the default path
                    }
                }]
            }
        ]
    },
    plugins: [
        new ExtractTextPlugin('styles.css')
    ]
};



module.exports = config;