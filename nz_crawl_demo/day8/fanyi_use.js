    var r = function(e) {
        var t = n.md5(navigator.appVersion),
        r = "" + (new Date).getTime(),
        i = r + parseInt(10 * Math.random(), 10);


        return {
            ts: r, //当前毫秒时间戳
            bv: t, //
            salt: i, //毫秒时间戳 与10以内的随机数字字符串进行拼接
            sign: n.md5("fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj")

        }
    };
    t.recordUpdate = function(e) {
        var t = e.i,
        i = r(t);
        n.ajax({
            type: "POST",
            contentType: "application/x-www-form-urlencoded; charset=UTF-8",
            url: "/bettertranslation",
            data: {
                i: e.i,//用户输入的5000字以内
                client: "fanyideskweb",
                salt: i.salt,
                sign: i.sign,
                ts: i.ts,
                bv: i.bv,
                tgt: e.tgt,
                modifiedTgt: e.modifiedTgt,
                from: e.from,
                to: e.to
            },
            success: function(e) {},
            error: function(e) {}
        })
    },