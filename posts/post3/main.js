var LIMIT = 130;

function primeFactorization(n) {
    var spf = new Array;
    spf.push(0);
    spf.push(1);
    for (var i = 2; i <= n; i++) {
        spf.push(i);
    }
    for (var i = 2; i <= n; i++) {
        if (spf[i] == i) {
            for (var j = i * i; j <= n; j+=i) {
                if (spf[j] == j) {
                    spf[j] = i;
                }
            }
        }
    }
    var primes = new Array;
    while (n != 1) {
        primes.push(spf[n]);
        n = Math.floor(n/spf[n]);
    }
    console.log(primes);
}

// var n = 128;
// primeFactorization(67);

var name = "Anand";
console.log(`${name}`, name);