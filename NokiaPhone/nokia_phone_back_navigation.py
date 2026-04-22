while True:
    print("""
1. Phone book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM services
0. Exit
""")

    choice = int(input("Select option: "))

    match choice:

        case 0:
            print("Goodbye")
            break

        case 1:
            while True:
                print("""
1. Search
2. Service Nos
3. Add name
4. Erase
5. Edit
6. Assign tone
7. Send b'card
8. Options
9. Speed dials
10. Voice tags
0. Back
""")
                phone_book = int(input("Select option: "))

                match phone_book:
                    case 0:
                        break
                    case 1:
                        print("Search")
                    case 2:
                        print("Service Nos")
                    case 3:
                        print("Add name")
                    case 4:
                        print("Erase")
                    case 5:
                        print("Edit")
                    case 6:
                        print("Assign tone")
                    case 7:
                        print("Send b'card")

                    case 8:
                        while True:
                            print("""
1. Type of View
2. Memory status
0. Back
""")
                            option = int(input("Select option: "))

                            match option:
                                case 0:
                                    break
                                case 1:
                                    print("Type of View")
                                case 2:
                                    print("Memory status")
                                case _:
                                    print("Invalid option")

                    case 9:
                        print("Speed dials")
                    case 10:
                        print("Voice tags")
                    case _:
                        print("Invalid option")

        case 2:
            while True:
                print("""
1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info service
9. Voice mailbox number
10. Service command editor
0. Back
""")
                messages = int(input("Select option: "))

                match messages:
                    case 0:
                        break
                    case 1:
                        print("Write messages")
                    case 2:
                        print("Inbox")
                    case 3:
                        print("Outbox")
                    case 4:
                        print("Picture messages")
                    case 5:
                        print("Templates")
                    case 6:
                        print("Smileys")

                    case 7:
                        while True:
                            print("""
1. Set 1
2. Common
0. Back
""")
                            message_settings = int(input("Select option: "))

                            match message_settings:
                                case 0:
                                    break

                                case 1:
                                    while True:
                                        print("""
1. Message centre number
2. Messages sent as
3. Message validity
0. Back
""")
                                        set1 = int(input("Select option: "))

                                        match set1:
                                            case 0:
                                                break
                                            case 1:
                                                print("Message centre number")
                                            case 2:
                                                print("Messages sent as")
                                            case 3:
                                                print("Message validity")
                                            case _:
                                                print("Invalid option")

                                case 2:
                                    while True:
                                        print("""
1. Delivery reports
2. Reply via same centre
3. Character support
0. Back
""")
                                        common = int(input("Select option: "))

                                        match common:
                                            case 0:
                                                break
                                            case 1:
                                                print("Delivery reports")
                                            case 2:
                                                print("Reply via same centre")
                                            case 3:
                                                print("Character support")
                                            case _:
                                                print("Invalid option")

                                case _:
                                    print("Invalid option")

                    case 8:
                        print("Info service")
                    case 9:
                        print("Voice mailbox number")
                    case 10:
                        print("Service command editor")
                    case _:
                        print("Invalid option")

        case 3:
            print("Chat")

        case 4:
            while True:
                print("""
1. Missed calls
2. Received calls
3. Dialled numbers
4. Erase recent call lists
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid credit
0. Back
""")
                call_register = int(input("Select option: "))

                match call_register:
                    case 0:
                        break
                    case 1:
                        print("Missed calls")
                    case 2:
                        print("Received calls")
                    case 3:
                        print("Dialled numbers")
                    case 4:
                        print("Erase recent call lists")

                    case 5:
                        while True:
                            print("""
1. Last call duration
2. All calls' duration
3. Received calls’ duration
4. Dialled calls’ duration
5. Clear timers
0. Back
""")
                            call_duration = int(input("Select option: "))

                            match call_duration:
                                case 0:
                                    break
                                case 1:
                                    print("Last call duration")
                                case 2:
                                    print("All calls' duration")
                                case 3:
                                    print("Received calls’ duration")
                                case 4:
                                    print("Dialled calls’ duration")
                                case 5:
                                    print("Clear timers")
                                case _:
                                    print("Invalid option")

                    case 6:
                        print("Show call costs")
                    case 7:
                        print("Call cost settings")
                    case 8:
                        print("Prepaid credit")
                    case _:
                        print("Invalid option")

        case 5:
            print("Tones")
        case 6:
            print("Settings")
        case 7:
            print("Call divert")
        case 8:
            print("Games")
        case 9:
            print("Calculator")
        case 10:
            print("Reminders")
        case 11:
            print("Clock")
        case 12:
            print("Profiles")
        case 13:
            print("SIM services")
        case _:
            print("Invalid menu choice")
