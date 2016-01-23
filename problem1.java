class Main {

	public static void main(Strings[] args) {
		int sum = 0;
		for(int x = 0; x < 1000; x = x+1) {
			if ((x % 3 == 0) || (x % 5 == 0)) {
				sum += x;
			}
		}

		System.out.print(sum);
	}
}
