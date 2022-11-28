function square(number) {
    return number * number;
}

function factorial(number){
    if (number == 0){
        return 0
    } else {
        return number * factorial(number)
    }
}

console.log(factorial(1))