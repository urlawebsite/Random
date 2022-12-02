function g(x){
    if (x==0){
        return 1
    
    }else{
        return x+2
    }
}

function f(t){
    if (1977 < t & t < 1984){
        return (2/7)*(t-1977)+12
    } else if (1984< t & t <= 1987) {
        return (t-1977)+7
    } else if (1987< t & t <= 1997){
        return (3/5)*(t-1977)+11
    } else{
        return "error: year"
    }
}

function h_0(t){
    var cost = 110/((1/2)*t+1)
    return cost
}

function h_1(t){
    costN = (((1/4)*(t**2)-1)**2)*26+52
    return costN
}

function h(t){
    var u = h_0(t)
    var d = h_1(t)
    return u & d
}

function q(d){
    var b = -d[1]
    var a = d[0]
    var c = d[2]
    var x1 = b + (Math.sqrt((b**2)-(4*a*c))/(2*a))
    var x2 = b - (Math.sqrt((b**2)-(4*a*c))/(2*a))
    return{"x1" : x1,"x2" : x2};
}

function eq(lst){
    var op = lst[1]
    var num1 = lst[0]
    var num2 = lst[2]
    var ans = lst[3]
    if (op == "+"){
        if ((num1 + num2) == ans)){
            return true
        } 
    } else if (op == "-"){
        if (num1 > num2){
            return num1 - num2
        } else if (num2 > num1){
            return num2-num1
        }else{
            return num1 - num2
        }
    } else if(op == "*"){
        return num1 * num2
    } else if (op == "/") {
        if (num1 > num2){
            if( (num1/num2) == ans){
                return true
            } else if ((num2/num1) == ans){
                return true
            } else{
                return false
            }
            
        }
    } else{
        return "Please add an operation, not a number"
    }
}

console.log(g(0))
console.log(g(1.01)) 
console.log(f(1976))
console.log(f(2000))
console.log(f(1988))
console.log(h(0))
console.log(q([-1,0,1]))
console.log(eq([14,"/",2,7]))
