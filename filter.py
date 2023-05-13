open('filtered_person_zinc.txt','a+').writelines([ line for line in open('provided.txt') if 'PER' in line])
