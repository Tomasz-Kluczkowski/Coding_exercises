const cleanInput = (input) => {
    const inputSet = new Set(input.split(','));
    const inputCleaned = [];
    for (let item of inputSet) {
        if ( item.length === 2 && !isNaN(item)) {
            inputCleaned.push(item);
        }

    }
    const inputSorter = {};
    //    sort input into rows
        for (let inputItem of inputCleaned) {
            if (inputSorter[inputItem[1]] !== undefined) {
                inputSorter[inputItem[1]].push(inputItem)
            } else {
                inputSorter[inputItem[1]] = [inputItem]
            }
        }
        const inputSorted = [];
    //    sort items in each row by columns now.
        for (let key of Object.keys(inputSorter)) {
            inputSorter[key].sort((a, b) => parseInt(a[0]) - parseInt(b[0]));
            inputSorted.push(...inputSorter[key])
        }
    return inputSorted
};

const findTerms = (item, input) => {
    const col = parseInt(item[0]);
    const row = parseInt(item[1]);
    const terms = [];
    const termsStr = [];
    terms.push([col - 1, row], [col, row + 1], [col + 1, row], [col, row - 1]);
    for (let term of terms) {
        term = term.join('');
        if (input.includes(term)) {
            termsStr.push(term)
        }
    }
    return termsStr
};


const buildPaths = (input, cache, pathNumber) => {
    for (let value of input) {
        const adjacentItems = findTerms(value, input);
        // check if there is a path already that can join with any of the adjacent items
        if (adjacentItems.length > 0) {
            for (let adjacentItem of adjacentItems) {
                // if we already saved an item to the path that is adjacent to this one, add the adjacent one to that path.
                const pathLookup = cache.seen[adjacentItem];
                // the path already exists - we add to it if not already there
                if (pathLookup !== undefined && !cache[pathLookup].includes(value)) {
                    cache[pathLookup].push(value);
                    cache.seen[value] = pathLookup;
                    break
                }
                // the path does not exist - make it
                cache[pathNumber] = [value];
                // save the path number belonging to the item added in seen
                cache.seen[value] = pathNumber;
                pathNumber += 1;
            }
        } else {
            cache[pathNumber] = [value];
            // save the path number belonging to the item added in seen
            cache.seen[value] = pathNumber;
            pathNumber += 1
        }
    }
    return cache
};


function solution(input) {
// remove duplicates and invalid inputs
    input = cleanInput(input);
    const cache = {seen: {}};
    let pathNumber = 0;
    const pathsCache = buildPaths(input, cache, pathNumber);
    let maxLength = 0;
    for (let key of Object.keys(pathsCache)) {
        if (key !== 'seen') {
            const pathLength = pathsCache[key].length;
            if (pathLength > maxLength) {
                maxLength = pathLength
            }
        }

    }
    console.log(maxLength);
    return maxLength
}

solution('11,32,21,12');
solution('18,00,95,40,36,26,57,48,54,65,76,87,97,47,00,46');