//
//  StandingsController.swift
//  redArmyApp
//
//  Created by Howard Zhao on 4/3/19.
//  Copyright © 2019 RedArmyApp. All rights reserved.
//

import UIKit

class StandingsController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        ///////////////////////////////////////////////////////////////////////
        //////////////////SWIPE LEFT AND SWIPE RIGHT GESTURES//////////////////
        ///////////////////////////////////////////////////////////////////////
        // LEFT SWIPE
        var leftSwipeGesture = UISwipeGestureRecognizer(target: self, action: #selector(receiveAndDoThis))
        leftSwipeGesture.direction = UISwipeGestureRecognizer.Direction.left
        self.view.addGestureRecognizer(leftSwipeGesture)
        // RIGHT SWIPE
        var rightSwipeGesture = UISwipeGestureRecognizer(target: self, action: #selector(receiveAndDoThis))
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
