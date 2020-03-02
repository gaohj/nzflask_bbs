var gulp = require("gulp")
var cssnano = require("gulp-cssnano")
var rename = require("gulp-rename")
var uglify = require("gulp-uglify")
var concat = require("gulp-concat")
var imagemin = require("gulp-imagemin")
var cache = require("gulp-cache")
gulp.task("greet",async()=>{
    await console.log("hello world")
})

//gulp greet 


//以上是4.0及以上版本  

//如果以下的版本 

// gulp.task('hell0',function(){
//     console.log("where are you");
// });   
//gulp hell0

//压缩css
gulp.task("css",async()=>{
    await gulp.src("./static/css/*.css") //找到css 源文件
    .pipe(cssnano())  //调用插件压缩 
    .pipe(gulp.dest("./dist/css/")) //压缩后的文件放到指定的目录 

});

//压缩并且改名字 css
gulp.task("cssrename",async()=>{
    await gulp.src("./static/css/*.css") //找到css 源文件
    .pipe(cssnano())  //调用插件压缩 
    .pipe(rename({'suffix':'.min'}))
    .pipe(gulp.dest("./dist/css/")) //压缩后的文件放到指定的目录 

});

//压缩并改名 js
gulp.task("js",async()=>{
    await gulp.src("./static/js/*.js") //找到js 源文件
    .pipe(uglify())  //调用插件压缩 
    .pipe(rename({'suffix':'.min'}))
    .pipe(gulp.dest("./dist/js/")) //压缩后的文件放到指定的目录 

});

//合并压缩及重命名  
gulp.task("concatjs",async()=>{
    // await gulp.src("./static/js/*.js")
    await gulp.src([
        './static/js/common.js',
        './static/js/index.js',
    ])
    .pipe(concat("index6.js"))
    .pipe(uglify())
    .pipe(rename({'suffix':'.min'}))
    .pipe(gulp.dest("./dist/js/"))
})

//压缩图片
gulp.task("img",async()=>{
     await gulp.src("./static/images/*.*")
    // .pipe(imagemin())  #无损压缩
    .pipe(cache(imagemin()))  //为了避免重复压缩 压缩以后放缓存中
    .pipe(rename({'suffix':'.min'}))
    .pipe(gulp.dest("./dist/images/"))
})



