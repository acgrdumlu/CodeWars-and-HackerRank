function process2Arrays(arr1, arr2) {
	let arr1NoDupes = arr1.filter(function(elem, index, self) {
		return index === self.indexOf(elem);
	});
	let arr2NoDupes = arr2.filter(function(elem, index, self) {
		return index === self.indexOf(elem);
	});

	let arr1Solo = arr1NoDupes.slice(0);
	let arr2Solo = arr2NoDupes.slice(0);
	function existsInBoth() {
		let count = 0;
		if (arr1NoDupes.length > 0 && arr2NoDupes.length > 0) {
			for (let a = 0, len = arr1NoDupes.length; a < len; a++) {
				if (arr2Solo.indexOf(arr1NoDupes[a]) > -1) {
					count++;
					let i = arr1Solo.indexOf(arr1NoDupes[a]);
					arr1Solo.splice(i, 1);
					i = arr2Solo.indexOf(arr1NoDupes[a]);
					arr2Solo.splice(i, 1);
				}
			}
		}
		return count;
	}

	let bothCount = existsInBoth();

	function existsInOne() {
		console.log(arr1NoDupes.length + " " + arr2NoDupes.length + " " + bothCount);
		return arr1NoDupes.length + arr2NoDupes.length - bothCount * 2;
	}


	return [bothCount, existsInOne(), arr1Solo.length, arr2Solo.length];
}