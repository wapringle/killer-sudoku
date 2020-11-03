circle = {surface: function(r){return 3.14 * r * r}}

function testme() {
    console.log("Hello Sailor");
}

function inx(x,l) {
    for(i=0;i<l.length;i++) if(x==l[i]) return true;
    return false;
}
function getSubTotals(target,numListList,sofar,use_exclude,exclude) {
    var s2=sofar;
    //console.log(target,numListList,sofar,use_exclude,exclude);
    if(numListList.length==0) {
        if(target==0) {
            var s3= s2.concat([exclude])
            return s3;
        }
                    
    } else {
        for(var j=0;j<numListList[0].length;j++) {
            var y=numListList[0][j];
            if(y>target) return s2;
            if(!(use_exclude && inx(y,exclude))) {
                var v=target-y;
                if(v>=0)
                    s2=getSubTotals(v,numListList.slice(1),s2,use_exclude,exclude.concat([y]));
            }
        }
    
    }
    return s2;
    
}

//console.log(getSubTotals(5,[[1, 2, 4], [1, 2, 4]],[],true,[]));
//console.log(getSubTotals(6,[[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],[],true,[]));
