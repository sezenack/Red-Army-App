//
//  ViewController.swift
//  redArmyApp
//
//  Created by gary on 2/22/19.
//  Copyright © 2019 RedArmyApp. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib
        
        //////////////////SWIPE LEFT AND SWIPE RIGHT GESTURES//////////////////
        
        // LEFT SWIPE
        let leftSwipeGesture = UISwipeGestureRecognizer(target: self, action: #selector(receiveAndDoThis))
        leftSwipeGesture.direction = .left
        self.view.addGestureRecognizer(leftSwipeGesture)
        // RIGHT SWIPE
        let rightSwipeGesture = UISwipeGestureRecognizer(target: self, action: #selector(receiveAndDoThis))
        rightSwipeGesture.direction = .right
        self.view.addGestureRecognizer(rightSwipeGesture)
    }
    
    // Take the gesture input and perform an action
    @objc func receiveAndDoThis(gesture: UISwipeGestureRecognizer) -> Void {
        if gesture.direction == UISwipeGestureRecognizer.Direction.left {
            print("segue to previous view")
        } else if gesture.direction == UISwipeGestureRecognizer.Direction.right {
            print("segue to next view")
        }
    }

    @IBAction func NewsButton(_ sender: Any) {
        
    }
    
    @IBAction func StandingsButton(_ sender: Any) {
    
    }
    
    @IBAction func ScheduleButton(_ sender: Any) {
        
    }
 
    @IBAction func StatsButon(_ sender: Any) {
    
    }
    

}

