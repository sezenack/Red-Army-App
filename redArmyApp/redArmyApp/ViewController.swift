//
//  ViewController.swift
//  redArmyApp
//
//  Created by gary on 2/22/19.
//

import UIKit

class ViewController: UIViewController {
	let segueTracker = 0
    override func viewDidLoad() {
        super.viewDidLoad()

		///////////////////////////////////////////////////////////////////////
        //////////////////SWIPE LEFT AND SWIPE RIGHT GESTURES//////////////////
        ///////////////////////////////////////////////////////////////////////
        // LEFT SWIPE
        var leftSwipeGesture = UISwipeGestureRecognizer(target: self, action: #selector(receiveAndDoThis))
        leftSwipeGesture.direction = UISwipeGestureRecognizer.Direction.Left
        self.view.addGestureRecognizer(leftSwipeGesture)
        // RIGHT SWIPE
        var rightSwipeGesture = UISwipeGestureRecognizer(target: self, action: #selector(receiveAndDoThis))
        rightSwipeGesture.direction = UISwipeGestureRecognizer.Direction.Right
        self.view.addGestureRecognizer(rightSwipeGesture)

    }

    // Take the swipe gesture input and perform an action
    @objc func receiveAndDoThis(_ gesture: UISwipeGestureRecognizer) -> Void {
        if gesture.direction == UISwipeGestureRecognizer.Direction.left {
			increment()
            print("segue to next view, swiped left")
        } else if gesture.direction == UISwipeGestureRecognizer.Direction.right {
			decrement()
            print("segue to previous view, swiped right")
        }
    }

	@objc func increment() {
		if segueTracker < 3 {
			segueTracker += 1
			print(segueTracker)
		}	
	}
	
	@objc func decrement() {
		if segueTracker > 0 {
			segueTracker -= 1
			print(segueTracker)
		}
	}
	
	///////////////////////////////////////////////////////////////////////
	//////////////////////////////BUTTON INPUT/////////////////////////////
	///////////////////////////////////////////////////////////////////////

    @IBAction func NewsButton(_ sender: Any) {
        print("News")
    }

    @IBAction func StandingsButton(_ sender: Any) {
		print("Standings")
    }

    @IBAction func ScheduleButton(_ sender: Any) {
		print("Schedule")
    }

    @IBAction func StatsButon(_ sender: Any) {
	    print("Stats")
    }

}
