
var firstUniqChar = function(s) {
    const dic = {};
    
    // Count occurrences of each character
    for (let i of s) {
        dic[i] = (dic[i] || 0) + 1;
    }

    // console.log(120||0,"adhahd") // answer is 120

    // Find the first unique character
    // const uniqueChar = Object.keys(dic).find(key => dic[key] === 1); // check the use of find method

    // using for loop
    for(let [i,j] of Object.entries(dic)){
        if(j===1){
            return s.indexOf(i);
        }
    }
    console.log(dic)
    return -1;
    // return uniqueChar !== undefined ? s.indexOf(uniqueChar) : -1;
};

console.log(firstUniqChar("ssomling"));
