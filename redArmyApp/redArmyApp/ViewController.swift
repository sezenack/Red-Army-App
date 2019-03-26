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
        let leftSwipeGesture = UISwipeGestureRecognizer(target: self, action: #selector(receiveAndDoThis))
        leftSwipeGesture.direction = .left
        self.view.addGestureRecognizer(leftSwipeGesture)
        // RIGHT SWIPE
        let rightSwipeGesture = UISwipeGestureRecognizer(target: self, action: #selector(receiveAndDoThis))
        rightSwipeGesture.direction = .right
        self.view.addGestureRecognizer(rightSwipeGesture)


    }

    // Take the swipe gesture input and perform an action
    @objc func receiveAndDoThis(gesture: UISwipeGestureRecognizer) -> Void {
        if gesture.direction == UISwipeGestureRecognizer.Direction.left {
            print("segue to next view")
        } else if gesture.direction == UISwipeGestureRecognizer.Direction.right {
            print("segue to next view")
        }
    }

	///////////////////////////////////////////////////////////////////////
	//////////////////////////////BUTTON INPUT/////////////////////////////
	///////////////////////////////////////////////////////////////////////

    @IBAction func NewsButton(_ sender: Any) {
        print("1")
    }

    @IBAction func StandingsButton(_ sender: Any) {
		print("2")
    }

    @IBAction func ScheduleButton(_ sender: Any) {
		print("3")
    }

    @IBAction func StatsButon(_ sender: Any) {
	    print("4")
    }

}
