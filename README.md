# IPL 2020 Prediction

    * Approach is to build a machine learning model based on the ICC's top 100 T20 batsmen,bowlers and allrounders rating points and their career data.
    * Scrape the data from ICC, cricbuzz which includes the current top 100 T20 batsmen,bowlers and allrounders and current IPL players of the each IPL team
    * Predict the rating points of each the IPL player(based on the his IPL career stats) by giving it the above built model
    * And then build a algorithm, when given two teams which has the predicted player rating points it will return the team that wins based on a logic 

## Authors 

	Name: Maharshi reddy Baddam
	NetID: MXB180036
 
	Name: Kalyan Kumar Kancharla
	NetID: KXK190004

## Steps to run

* The below commands scrapes the data using beautiful soap
    	

python scrap.py	
python ipl_scrap.py


* Run the below command that build ML model and uses the above scraped IPL data to predict the winner of IPL
    

python ipl_prediction.py
