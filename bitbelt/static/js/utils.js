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
    if(word) {
        const words = word.split(' ');

        const finalVersion = words.map(w => w[0].toUpperCase() + w.slice(1).toLowerCase()).join(' ');
        return finalVersion;
    }
}

const combineObjectKeysAddValues = (arrayOfObjects) => {
    let result = {};

    arrayOfObjects.forEach((val, index) => {
        val.forEach((val2, index2) => {
            const keys = Object.keys(val2);

            keys.forEach((key, index) => {
                if(result.hasOwnProperty(key)) {
                    result[key] += val2[key];
                } else {
                    result[key] = val2[key];
                }
            });
        });
    });

    return result;
};

export {
    formatMomentDate,
    momentFormat,
    convertDecimalToFraction,
    capitalizeFirstLetterOfEachWordAndLowercaseAllOthers,
    combineObjectKeysAddValues
};