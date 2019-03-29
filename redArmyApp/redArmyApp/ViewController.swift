//
//  ViewController.swift
//  redArmyApp
//
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
        leftSwipeGesture.direction = UISwipeGestureRecognizerDirection.Left
        self.view.addGestureRecognizer(leftSwipeGesture)
        // RIGHT SWIPE
        var rightSwipeGesture = UISwipeGestureRecognizer(target: self, action: #selector(receiveAndDoThis))
        rightSwipeGesture.direction = UISwipeGestureRecognizerDirection.Right
        self.view.addGestureRecognizer(rightSwipeGesture)

    }

    // Take the swipe gesture input and perform an action
    @objc func receiveAndDoThis(_ gesture: UISwipeGestureRecognizer) -> Void {
        if gesture.direction == UISwipeGestureRecognizer.Direction.left {
            print("segue to next view, swiped left")
        } else if gesture.direction == UISwipeGestureRecognizer.Direction.right {
            print("segue to previous view, swiped right")
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
