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
    @objc func receiveAndDoThis(gesture: UIGestureRecognizer) {
        if let swipeGesture = gesture as? UISwipeGestureRecognizer {
            switch swipeGesture.direction {
                case UISwipeGestureRecognizerDirection.Right:
                    print("right")
                case UISwipeGestureRecognizerDirection.Left:
                    print("left")
            }
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
