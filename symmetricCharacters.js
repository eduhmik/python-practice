function solution(s) {
    let solution = 0;
    helper(s, "").forEach(str => {
        solution = Math.max(solution, longestSymmetrical(str));
    });
    return solution;
}

function helper(st, p) {
    let solution = [];
    if (st === "") return [p];
    if (st[0] === "?") {
        solution = solution.concat(helper(st.substring(1), p + "<"));
        solution = solution.concat(helper(st.substring(1), p + ">"));
    } else {
        solution = solution.concat(helper(st.substring(1), p + st[0]));
    }
    return solution;
}

function longestSymmetrical(st) {
    let stack = [];
    let ans = 0;
    let counter = 0;
    for (let c of st) {
        if (c === "<") {
            counter = 0;
            stack.push(c);
        } else {
            if (stack.length !== 0) {
                counter += 2;
                stack.pop();
                ans = Math.max(ans, counter);
            }
        }
    }
    return ans;
}

let str = "<><?";
console.log(solution(str)); 