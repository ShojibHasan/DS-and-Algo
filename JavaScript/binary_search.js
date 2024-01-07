function binarySearch(list,target){
    let low = 0;
    let high = list.length - 1;
    while(low<=high){
        let mid = Math.floor((low+high)/2);
        let guess = list[mid];
        if (guess == target){
            return mid;
        }else if (guess > target){
            high = mid -1;
        }else{
            low = mid+1;
        }
    }
    return -1;
}
const list = [11,22,33,44,55,66,77,88,99,111,122,133,144,155,166,177,188,199]
const target = 111
console.log(binarySearch(list,target))