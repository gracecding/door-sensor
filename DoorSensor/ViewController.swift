//
//  ViewController.swift
//  DoorSensor
//
//  Created by Grace Ding on 3/12/18.
//  Copyright © 2018 Grace Ding. All rights reserved.
//

import UIKit
import Firebase
import FirebaseDatabase

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func led(state: String) {
        let ref = FIRDatabase.database().reference()
        
    }


}

