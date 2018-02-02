import math from 'mathjs';

const convertDecimalToFraction = function(decimal) {
    const value = math.fraction(decimal);
    let numerator = value.n;
    let denomenator = value.d;

    let whole = (numerator - (numerator % denomenator)) / denomenator;
    let mixedNumerator = numerator % denomenator;
    let mixedDenomenator = denomenator;

    return `${whole}${mixedNumerator > 0 ? ` ${mixedNumerator}/${mixedDenomenator}` : ''}`;
}

export { convertDecimalToFraction };