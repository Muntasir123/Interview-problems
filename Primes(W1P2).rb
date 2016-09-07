puts "Enter some number you want to go to"
num = gets.to_i
prime = 1
prime_add = Math.log(2)
while(prime < num)
	prime+=2
	prime_add+=Math.log(prime) if (2..Math.sqrt(prime+1)).each do |k|
		break if prime%k==0
	end
end
puts prime_add / num