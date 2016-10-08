function process2Arrays(arr1, arr2) {
	let arr1Set = new Set(arr1);
	let arr2Set = new Set(arr2);

	// Set intersections contain only items from both sets
	let intersection = new Set([...arr1Set].filter(x => arr2Set.has(x)));

	// Set difference contain only items from first list, not in second list
	let diffArr1 = new Set([...arr1Set].filter(x => !arr2Set.has(x)));
	let diffArr2 = new Set([...arr2Set].filter(x => !arr1Set.has(x)));

	return [intersection.size, diffArr1.size + diffArr2.size, diffArr1.size, diffArr2.size];
}