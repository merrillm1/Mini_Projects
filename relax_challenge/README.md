## Results

The aim of this challenge is to predict the factors that contribute most to user adoption. User adoption here is defined as a user who has logged in at least three times within *any* 7 day period. Factors here include the following:

    - name:  the  user's  name
    - object_id:   the  user's  id
    - email:  email  address
    - creation_source:   how  their  account  was  created.  This  takes  on  one
      of  5  values:
        - PERSONAL_PROJECTS:  invited  to  join  another  user's
          personal  workspace
        - GUEST_INVITE:  invited  to  an  organization  as  a  guest
          (limited  permissions)
        - ORG_INVITE:  invited  to  an  organization  (as  a  full  member)
        - SIGNUP:  signed  up  via  the  website
        - SIGNUP_GOOGLE_AUTH:  signed  up  using  Google
    - Authentication  (using  a  Google  email  account  for  their  login id)
    - creation_time:  when  they  created  their  account
    - last_session_creation_time:   unix  timestamp  of  last  login
    - opted_in_to_mailing_list:  whether  they  have  opted  into  receiving
      marketing  emails
    - enabled_for_marketing_drip:  whether  they  are  on  the  regular
      marketing  email  drip
    - org_id:   the  organization  (group  of  users)  they  belong  to
    - invited_by_user_id:   which  user  invited  them  to  join  (if  applicable).

A second dataframe was also provided which details each users activity. 

Feature selection was made using an SVM model, as our dataframe was relatively small (<10^5) and sparse. The SVM model was also chosen for its ability to find the maximal margin between a nonlinear approximator. 

The results here suggest that the user length and and being opted in to the mailing list are among the most significant indicators of a user becoming adopted. Exploratory data analysis revealed a slight correlation between how a user was created and whether they became adopted, this was also reflected in the model results. Those invited by an organization or a guest were also strong indicators of adoption. 

I do have a few reservations about these results however. It is natural to assume that a longer time frame for a user would open greater opportunities for them to become adopted. For those who had signed up towards the end of the documented period, the likelihood that they became adopted reduced, as evidenced by a time series plot in the notebook. More work can be done here to limit the engagements to those who have been enrolled for at least a designated time period. 

The model results seemed promising. The accuracy for the SVM model was 96% and the AUROC was close to perfect. The data here was highly imbalanced however, so the more appropriate evaluation metric here is the F1 score, our model gave an F1 score of approximately an 87%. 