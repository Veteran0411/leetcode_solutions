
var firstUniqChar = function(s) {
    const dic = {};
    
    // Count occurrences of each character
    for (let i of s) {
        dic[i] = (dic[i] || 0) + 1;
    }

    // Find the first unique character
    const uniqueChar = Object.keys(dic).find(key => dic[key] === 1); // check the use of find method

    return uniqueChar !== undefined ? s.indexOf(uniqueChar) : -1;
};

console.log(firstUniqChar("ssomling"));
