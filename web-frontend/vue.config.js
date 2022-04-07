const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '^/': { 
        target: "http://140.116.249.231:8000",
        ws: false, 
        changeOrigin: true 
      }
    }
  },
});
