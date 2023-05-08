let c = 0;

function GCD(k, l){
    while(k!=l){
        if(k > l){
            k = k - l;
        }else{
            l = l - k;
        }
    c++;
    }
    return k;
}

let a = 66528;
let b = 52920;

let result = GCD(a,b);
console.log(result);