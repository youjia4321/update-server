module.exports = {
    assetsDir: 'static',
    chainWebpack: config => {
        config
            .entry('index')
            .add('babel-polyfill')
    }
};
