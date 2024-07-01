// check this later

const revString=(s)=>{
    let l=0;
    let h=s.length-1;

    // let arr=Array(s.length).fill("0");
    let arr=s.split("");
    while(l<=h){
        if(!(/[a-zA-Z]/.test(s[l]))){
            l++;
        }
        else if(!(/[a-zA-Z]/.test(s[h]))){
            h--;
        }else{
            [arr[l],arr[h]]=[arr[h],arr[l]]
            l++;
            h--;
        }
    }
    console.log(arr.join(""))
}

let s="h@ello$#"
revString(s)