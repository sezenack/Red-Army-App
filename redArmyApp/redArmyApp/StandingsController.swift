//
//  StandingsController.swift
//  redArmyApp
//
//  Created by Howard Zhao on 4/3/19.
//  Copyright © 2019 RedArmyApp. All rights reserved.
//

import UIKit

class StandingsController: UIViewController, UITableViewDataSource, UITableViewDelegate {
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return textarray.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "ECACStandings", for: indexPath)
        //if indexPath.item > 1 {
            //cell.textLabel?.font = UIFont (name: "Arial", size: 10.0)
        //}
        cell.textLabel?.text = textarray[indexPath.item]
        return cell
    }
    
    let StandingsHTMLString : String
    let StandingsURL : NSURL
    let StandingsString : String
    
    required init(coder aDecoder: NSCoder) {
        self.StandingsHTMLString = "https://www.ecachockey.com/men/2018-19/standings"
        self.StandingsURL = NSURL(string: StandingsHTMLString)!
        do {
            self.StandingsString = try String(contentsOf: StandingsURL as URL)
        } catch let error {
            self.StandingsString = ""
            print("Error: \(error)")
        }
        super.init(coder: aDecoder)!
    }
    
    let textarray = ["\t\t\tECAC Standings 2018-2019", "  Team\t\t\tPts\tGP\tW-L-T\tPCT\tGF\tGA", "1  Quinnipiac\t30\t22\t14-6-2\t0.682\t77\t47", "2  Cornell\t\t30\t22\t13-5-4\t0.682\t64\t41", "3  Clarkson\t28\t22\t13-7-2\t0.636\t65\t42", "4  Harvard\t\t28\t22\t13-7-2\t0.636\t77\t58", "5  Dartmouth\t23\t22\t10-9-3\t0.523\t53\t55", "6  Yale\t\t\t23\t22\t11-10-1\t0.523\t53\t57", "7  Union\t\t22\t22\t10-10-2\t0.500\t60\t64", "8  Brown\t\t21\t22\t8-9-5\t0.477\t52\t59", "9  Princeton\t18\t22\t8-12-2\t0.409\t60\t66", "10 Colgate\t\t17\t22\t7-12-3\t0.386\t43\t64", "11 RPI\t\t\t16\t22\t7-13-2\t0.364\t49\t67", "12 SLU\t\t\t8\t22\t3-17-2\t0.182\t51\t84"]
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        ///////////////////////////////////////////////////////////////////////
        //////////////////SWIPE LEFT AND SWIPE RIGHT GESTURES//////////////////
        ///////////////////////////////////////////////////////////////////////
        // LEFT SWIPE
        let leftSwipeGesture = UISwipeGestureRecognizer(target: self, action: #selector(receiveAndDoThis))
        leftSwipeGesture.direction = UISwipeGestureRecognizer.Direction.left
        self.view.addGestureRecognizer(leftSwipeGesture)
        // RIGHT SWIPE
        let rightSwipeGesture = UISwipeGestureRecognizer(target: self, action: #selector(receiveAndDoThis))
        rightSwipeGesture.direction = UISwipeGestureRecognizer.Direction.right
        self.view.addGestureRecognizer(rightSwipeGesture)
        
    }
    
    // Take the swipe gesture input and perform an action
    @objc func receiveAndDoThis(_ gesture: UISwipeGestureRecognizer) -> Void {
        if gesture.direction == UISwipeGestureRecognizer.Direction.left {
            print("segue to next view, swiped left")
            performSegue(withIdentifier: "Stats", sender: self)
            
        } else if gesture.direction == UISwipeGestureRecognizer.Direction.right {
            print("segue to previous view, swiped right")
            performSegue(withIdentifier: "News", sender: self)
        }
        
    }
    
    ///////////////////////////////////////////////////////////////////////
    //////////////////////////////BUTTON INPUT/////////////////////////////
    ///////////////////////////////////////////////////////////////////////
    
   
    @IBAction func NewsButton(_ sender: Any) {
        print("News2")
        performSegue(withIdentifier: "News", sender: self)
    }
    
    @IBAction func StatsButton(_ sender: Any) {
        print("Stats2")
        performSegue(withIdentifier: "Stats", sender: self)
    }
    
    @IBAction func ScheduleButton(_ sender: Any) {
        print("Schedule2")
        performSegue(withIdentifier: "Schedule", sender: self)
    }
}
