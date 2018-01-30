const webpack = require('webpack');
const path = require('path');

const config = {
    entry:  {
        index: path.join(__dirname, 'js', 'index.js'),
        'project-list': path.join(__dirname, 'js', 'pages', 'project-list.js'),
        project: path.join(__dirname, 'js', 'pages', 'project.js')
    },
    output: {
        path: path.join(__dirname, 'dist'),
        filename: '[name].bundle.js',
    },
    resolve: {
        extensions: ['.js', '.css']
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: 'babel-loader'
            }
        ]
    }
};



module.exports = config;