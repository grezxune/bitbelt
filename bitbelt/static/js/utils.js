import math from 'mathjs';
import moment from 'moment';

const momentFormat = "dddd, MM/DD/YYYY, h:mm:ss a";

const formatMomentDate = (millis) => {
    return moment(millis).format(momentFormat);
}

const convertDecimalToFraction = function(decimal) {
    const value = math.fraction(decimal);
    let numerator = value.n;
    let denomenator = value.d;

    let whole = (numerator - (numerator % denomenator)) / denomenator;
    let mixedNumerator = numerator % denomenator;
    let mixedDenomenator = denomenator;

    return `${whole}${mixedNumerator > 0 ? ` ${mixedNumerator}/${mixedDenomenator}` : ''}`;
}

const capitalizeFirstLetterOfEachWordAndLowercaseAllOthers = (word) => {
    const words = word.split(' ');

    const finalVersion = words.map(w => w[0].toUpperCase() + w.slice(1).toLowerCase()).join(' ');
    return finalVersion;
}

export {
    formatMomentDate,
    momentFormat,
    convertDecimalToFraction,
    capitalizeFirstLetterOfEachWordAndLowercaseAllOthers
};