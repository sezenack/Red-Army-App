//
//  ViewController.swift
//  redArmyApp
//  News Controller
//  Created by gary on 2/22/19.
//

import UIKit

class ViewController: UIViewController {

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
            performSegue(withIdentifier: "Standings", sender: self)
        } else if gesture.direction == UISwipeGestureRecognizer.Direction.right {
            print("segue to previous view, swiped right")
            performSegue(withIdentifier: "Schedule", sender: self)
        }
        
    }
    
	///////////////////////////////////////////////////////////////////////
	//////////////////////////////BUTTON INPUT/////////////////////////////
	///////////////////////////////////////////////////////////////////////
    
    @IBAction func StandingsButton(_ sender: Any) {
		print("Standings")
        performSegue(withIdentifier: "Standings", sender: self)
    }

    @IBAction func ScheduleButton(_ sender: Any) {
		print("Schedule")
        performSegue(withIdentifier: "Schedule", sender: self)
    }

    @IBAction func StatsButon(_ sender: Any) {
	    print("Stats")
        performSegue(withIdentifier: "Stats", sender: self)
    }

}
