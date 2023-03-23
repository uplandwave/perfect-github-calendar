cd $HOME/Documents/GitHub/perfect-github-calendar
for i in {0..15}; do
	date >> always-green.txt
	git add .
	git commit -m "Fake News"
	git push
done
