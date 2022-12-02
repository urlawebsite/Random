
function c(r,h){
  return (1/3)*Math.PI*(r**2)*h
}

function f(t){
  var num = (t**2) + 10*t + 100
  var denom =(t**2)+ 20*t + 100 
  return 100*(num/denom) 
} 

function p(t){
    var Percentage = 0.0135*(t**4) - 0.49375*(t**3) + 2.58333*(t**2) + 3.8*t + 31.60704
    return Percentage
}

function cost(x){
  var k = 0.5*x
  var p = 100-x
  return k/p
}

function D(t,a){
  var r = t+1
  var e = 24
  return (r/e)*a
}




console.log(c(2,5))
console.log(f(0))
console.log(p(0))
console.log(cost(50))
console.log(D(4, 500))