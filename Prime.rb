prime = 1
prime_count = 1
while (prime_count < 1000)
	prime+=2
	prime_count+=1 if (2..Math.sqrt(prime+1)).each do |k|
		break if prime % k == 0
	end
end
puts prime